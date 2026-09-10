---
layout: default
title: Magnesium Hydroxide
parent: 高證據等級 (L1-L2)
nav_order: 470
evidence_level: L2
indication_count: 5
---

# Magnesium Hydroxide
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Magnesium Hydroxide（氫氧化鎂）：從制酸劑用途到消化性潰瘍治療

## 一句話總結

Magnesium Hydroxide 是傳統制酸劑成分，長期用於中和胃酸、緩解消化不良症狀。
TxGNN 模型預測它對**消化性潰瘍（Active Peptic Ulcer Disease）**的關聯分數高達 **99.98%**，
目前雖無直接臨床試驗登記，但有 **20 篇文獻**支持，且此機轉早已是制酸劑數十年臨床實務的常識，並非全新假說。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無正式登記資料可查（本品於香港未上市）；傳統上作為制酸劑用於胃酸過多／消化不良 |
| 預測新適應症 | 消化性潰瘍（Active Peptic Ulcer Disease） |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏結構化的作用機轉（MOA）欄位資料，但證據包中的機轉關聯說明已提供足夠資訊：Mg(OH)₂ 屬於制酸劑，作用是中和胃酸、提高胃內 pH、降低胃蛋白酶活性，並促進黏膜前列腺素與表皮生長因子（EGF）相關的細胞保護機轉。

原適應症（制酸劑用於胃酸過多／消化不良）與預測新適應症（活動性消化性潰瘍）在機轉上高度重疊——制酸劑正是消化性潰瘍治療的傳統一線藥物之一，這項預測反映的是數十年臨床使用累積下來的既有知識，而非 TxGNN 憑空產生的全新假說。

值得注意的是，本次證據包中排名第 2～5 的預測（吻合口潰瘍、潰瘍穿孔、胃十二指腸炎、胃潰瘍）同屬酸相關消化道疾病家族，形成一個機轉一致的預測群集，進一步強化了「制酸劑→酸相關潰瘍疾病」這條路徑的可信度；但其中證據強弱不一（例如潰瘍穿孔僅有 1 篇個案觀察文獻、評等 L4，建議為 Hold），顯示模型對同一藥理家族內不同病名的區分度仍有限。

## 臨床試驗證據

目前無相關臨床試驗登記。

*註：同一證據包中排名第 5 的「胃潰瘍」預測有 1 個相關試驗登記（NCT07310927），但該試驗比較的是 alginate 與 sucralfate 併用 PPI 治療 GERD 症狀，非本藥物、亦非以消化性潰瘍為主要適應症，相關性評為 C 級（低），僅供參考。*

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT | Scand J Gastroenterol | 72 名十二指腸/幽門前潰瘍患者雙盲試驗：制酸劑+抗膽鹼藥 3 週癒合率 50%，優於安慰劑 |
| [1526089](https://pubmed.ncbi.nlm.nih.gov/1526089/) | 1992 | RCT | Clin Pharmacol Ther | Nizatidine 對比安慰劑治療良性胃潰瘍的多中心雙盲試驗 |
| [22950493](https://pubmed.ncbi.nlm.nih.gov/22950493/) | 2013 | Review | Curr Pharm Des | 回顧制酸劑透過前列腺素以外機轉達成胃黏膜保護與潰瘍癒合的細胞與分子機轉 |
| [6086186](https://pubmed.ncbi.nlm.nih.gov/6086186/) | 1984 | Review/Comparative | Clin Gastroenterol | 回顧制酸劑與抗膽鹼藥於十二指腸潰瘍治療中的角色與藥理特性 |
| [2595273](https://pubmed.ncbi.nlm.nih.gov/2595273/) | 1989 | 動物實驗 | Scand J Gastroenterol | 大鼠實驗顯示含 Mg(OH)₂/Al(OH)₃ 制酸劑對多種誘發性胃損傷有劑量依賴性保護作用 |
| [37146](https://pubmed.ncbi.nlm.nih.gov/37146/) | 1979 | 綜述 | Fortschritte der Medizin | 綜述制酸劑於消化性潰瘍的中和胃酸與抑制胃蛋白酶活性機轉及給藥時機 |
| [2390927](https://pubmed.ncbi.nlm.nih.gov/2390927/) | 1990 | 動物實驗 | Dig Dis Sci | 大鼠模型顯示制酸劑（含 Al(OH)₃ 成分）促進前列腺素/EGF 相關的慢性胃十二指腸潰瘍癒合 |
| [1769429](https://pubmed.ncbi.nlm.nih.gov/1769429/) | 1991 | 動物實驗 | Digestion | 探討含鋁制酸劑對急性胃黏膜病灶的保護作用與胃內 pH 的關係 |
| [9305482](https://pubmed.ncbi.nlm.nih.gov/9305482/) | 1997 | 臨床研究 | Aliment Pharmacol Ther | 十二指腸潰瘍患者中，H2 受體拮抗劑與制酸劑可能加重幽門螺旋桿菌胃炎 |
| [8260735](https://pubmed.ncbi.nlm.nih.gov/8260735/) | 1993 | 綜述 | J Physiol Pharmacol | 綜述含鎂/鋁制酸劑降低胃酸與胃蛋白酶活性，並具細胞保護作用的臨床藥理新進展 |

## 香港上市資訊

目前無香港上市許可證資料（本藥品於香港未上市，登記數為 0）。

## 安全性考量

安全性資訊請參考原廠仿單。

*註：本評估目前缺乏仿單警語/禁忌資料（DG001，Blocking），這是進入安全性初評（S1）前必須補齊的關鍵缺口。*

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 制酸劑中和胃酸、促進黏膜保護的機轉與消化性潰瘍治療高度契合，且有 1 篇直接針對活動性潰瘍的 RCT（Ström 1981）及多篇支持性文獻佐證，證據等級達 L2。
- 但本藥品目前於香港未上市，且仿單警語/禁忌資料缺失（DG001，Blocking），在補齊安全性資料前無法完成 S1 初評。

**若要推進需要：**
- 取得仿單/官方安全性資料（警語、禁忌、DDI），解除 DG001 阻斷性缺口
- 透過 DrugBank API 查詢確認正式 MOA 描述（DG002）
- 若考慮於香港推進，需先確認上市/進口許可路徑（目前 0 張許可證）
- 針對排名 2～5 的相關預測（尤其潰瘍穿孔、吻合口潰瘍），因證據薄弱（L3–L4），暫列為研究性問題，不建議與主要適應症並行推進
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Cimetidine
parent: 僅模型預測 (L5)
nav_order: 198
evidence_level: L5
indication_count: 9
---

# Cimetidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Cimetidine：從消化性潰瘍到全身性肥大細胞增生症（惰性型）

## 一句話總結

Cimetidine（西咪替丁）是 H2 受體拮抗劑，原本用於胃潰瘍、十二指腸潰瘍、胃食道逆流及 Zollinger-Ellison 症候群等胃酸相關疾病。
TxGNN 模型預測它可能對**惰性全身性肥大細胞增生症 (Smouldering systemic mastocytosis)** 有效，但目前**沒有臨床試驗與文獻**直接支持，屬於純模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃潰瘍、胃食道逆流、十二指腸潰瘍、Zollinger-Ellison 症候群等（取自知識圖譜） |
| 預測新適應症 | 惰性全身性肥大細胞增生症 (Smouldering systemic mastocytosis) |
| TxGNN 預測分數 | 99.80% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Cimetidine 為 H2 受體拮抗劑，可抑制胃酸分泌。

在知識圖譜中，Cimetidine 已與全身性肥大細胞增生症 (systemic mastocytosis) 有適應症關聯。肥大細胞釋放的組織胺會刺激胃酸過度分泌，造成腸胃道症狀，H2 阻斷可緩解這類症狀。TxGNN 的高分很可能反映了這層既有關聯。

但這僅限於**症狀控制**，沒有疾病修飾（disease-modifying）的依據。針對惰性亞型，目前沒有任何試驗或文獻佐證，因此不應視為真正的新適應症。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 其他預測適應症概覽

以下為排名第 2 至第 9 的預測，僅供參考，皆未達進一步推進的證據強度：

| 排名 | 預測適應症 | 分數 | 證據等級 | 說明 |
|-----|-----------|------|---------|------|
| 2 | 活動性消化性潰瘍 | 99.79% | L4 | 實質上屬既有適應症，非真正再利用。文獻多為其他藥物的回顧，僅 1981 年一項（[PMID 7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/)）比較 Cimetidine 與安慰劑，結果未提供 |
| 3 | 消化性潰瘍穿孔 | 99.77% | L4 | 文獻多為「使用 Cimetidine 期間仍發生穿孔」的病例報告，屬安全性或失敗訊號，非療效證據 |
| 4 | 胃空腸潰瘍 | 99.77% | L4 | 僅有消化性潰瘍的一般性回顧與評論，屬間接推論 |
| 5 | 淋巴結病變性肥大細胞增生症伴嗜酸性球增多 | 99.76% | L5 | 無試驗或文獻，僅為模型預測 |
| 6 | 十二指腸胃逆流 | 99.49% | L4 | 僅有小型生理學研究（如 [PMID 4018640](https://pubmed.ncbi.nlm.nih.gov/4018640/)），無臨床獲益證據 |
| 7 | 十二指腸阻塞 | 99.44% | L4 | 僅有病例層級觀察（[PMID 361048](https://pubmed.ncbi.nlm.nih.gov/361048/)），結構性阻塞預期無效 |
| 8 | 痤瘡 | 99.33% | L4 | Cimetidine 具微弱抗雄性素作用，機轉上有可能，但證據間接且效果有限，較適合列為研究問題 |
| 9 | 升糖素分泌異常 | 99.14% | L5 | 唯一文獻為 Meckel 憩室造影研究，與此適應症無關 |

---

## 香港上市資訊

香港共有 20 張有效的單方許可證，以下列出 5 張主要許可證（資料中未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-41813 | TAMEDIN F C TAB 400MG | KAI YUEN PHARMACEUTICAL CO |
| HK-47776 | ULCIMET 400 TAB 400MG | NATURAL HEALTH RESOURCES COMPANY LIMITED |
| HK-38804 | STOMCAP-1 TAB 200MG | LOYAL ADVANCE LIMITED |
| HK-65798 | SANWELL TABLETS 200MG | HITPHARM PHARMACEUTICAL CO LTD |
| HK-63341 | SYNGAMET TABLET 200MG | EUROPHARM LAB CO LTD |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（非仿單內容）：肝臟疾病、膽囊疾病、腎功能不全、胃癌（含胃腺癌、瀰漫性胃腺癌、皮革胃等）。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 中度：Paclitaxel、Fentanyl、Acalabrutinib、Lidocaine、Acebutolol、Dihydrocodeine、Codeine、Tramadol、Nifedipine、Alfentanil
  - 輕度：Dolutegravir、Zidovudine、Acetaminophen、Ketorolac、Ibuprofen、Ethinylestradiol 等
- 文獻中另提及使用 H2 拮抗劑於壓力性潰瘍預防時，院內肺炎風險可能增加（[PMID 8250708](https://pubmed.ncbi.nlm.nih.gov/8250708/)）。

仿單的警語與禁忌資料尚未取得，其餘安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測（惰性全身性肥大細胞增生症）沒有任何試驗或文獻支持，證據等級僅 L5。Cimetidine 在此最多是症狀性輔助，且該疾病已屬原適應症範疇，並非新的治療用途。
- 其餘高分預測多為既有適應症的延伸，或僅有間接、低品質證據，部分文獻甚至顯示是安全性或失敗訊號。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌資料（目前屬阻擋性資料缺口）
- 補充 Cimetidine 的作用機轉資料（可查詢 DrugBank）
- 針對肥大細胞增生症各亞型，系統性搜尋 H2 拮抗劑的臨床研究
- 若考慮痤瘡等皮膚科用途，需與現有標準療法比較其療效與必要性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


---
layout: default
title: Calcitriol
parent: 僅模型預測 (L5)
nav_order: 144
evidence_level: L5
indication_count: 7
---

# Calcitriol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Calcitriol：從活性維生素 D 製劑到維生素 D 缺乏症

## 一句話總結

Calcitriol 是維生素 D 的活性形式，在香港已有 8 張許可證，但資料中沒有載明原適應症。
TxGNN 模型預測它可能對**維生素 D 缺乏症（obsolete vitamin D deficiency）**有效，分數很高（99.96%）。
不過這個預測目前**沒有任何臨床試驗或文獻支持**，屬於純模型預測（L5）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 維生素 D 缺乏症（obsolete vitamin D deficiency，本體論中已標為過時術語） |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Calcitriol 是維生素 D 的活性形式（1,25-二羥維生素 D3），所以與維生素 D 缺乏症在生物學上有明顯關聯：直接補充活性形式，理論上可以彌補缺乏的部分。

這個預測需要保留幾點：

- 「維生素 D 缺乏症」在本體論中被標為 **obsolete（過時）**，可能是舊詞或已被合併的詞條，預測分數可能只反映術語本身。
- 預測與原適應症的相似度分析尚待完成。
- 沒有任何試驗或文獻直接驗證，因此這個分數只能視為假說的起點。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 其他預測適應症的證據

第一順位的預測缺乏證據，但同一份資料中的其他預測有較多支持。以下僅供參考，不影響上方的主要評估。

| 排名 | 預測適應症 | 分數 | 證據等級 | 證據概況 |
|------|-----------|------|---------|---------|
| 7 | 遺傳性低磷佝僂症（hereditary hypophosphatemic rickets） | 99.28% | L3 | 7 個試驗、20 篇文獻，機轉直接相關 |
| 2 | 腎小管酸中毒（renal tubular acidosis） | 99.93% | L4 | 19 篇文獻，多為病例報告與生理研究，屬間接證據 |
| 6 | Dahlberg-Borer-Newcomer syndrome | 99.76% | L4 | 文獻多談相關鈣磷代謝疾病，未直接談此症候群 |
| 3、4、5 | 家族性孤立性副甲狀腺低下症、Campailla-Martinelli 型肢中發育不良、顱面錐形發育不良 | 99.78%–99.81% | L5 | 無試驗、無文獻 |

遺傳性低磷佝僂症的機轉最合理：FGF23 過多會抑制腎臟 CYP27B1，使內源性 1,25(OH)2D 下降，補充 calcitriol 可取代缺少的活性荷爾蒙。相關試驗中與 calcitriol 最直接的兩項如下：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) | Early Phase 1 | 進行中（不再招募） | 20 | Calcitriol 單獨治療 X 染色體連鎖低磷血症，觀察礦物質離子、生長與骨骼指標 |
| [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) | Phase 4 | 未知 | 100 | 比較高、低劑量活性維生素 D 併用中性磷酸鹽於 XLH 兒童（是否為 calcitriol 需自標題以外確認） |

以上試驗均未提供療效結果。另有一項 Phase 3 試驗（[NCT06046820](https://clinicaltrials.gov/study/NCT06046820)，INZ-701 用於 ENPP1 缺乏症），其中 calcitriol 是否為對照或背景治療無法從現有資料確認。

## 香港上市資訊

香港共有 8 張 calcitriol 許可證，以下列出 5 張。資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-65345 | OSTOVEL CAPSULES 0.25MCG | HEALTHCARE PHARMASCIENCE LIMITED |
| HK-57635 | CALCITRIOL-DP 0.25MCG CAP | UNITED ITALIAN CORP (HK) LTD |
| HK-52239 | OSTEODIOL CAP 0.25MCG | TEVA PHARMACEUTICAL HONG KONG LIMITED |
| HK-52238 | OSTEODIOL CAP 0.5MCG | TEVA PHARMACEUTICAL HONG KONG LIMITED |
| HK-05357 | ROCALTROL CAP 0.25UG | PRUDENTLINK LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。DDI 查詢未找到相關資料。

## 結論與下一步

**決策：Hold**

**理由：**
- 第一順位的預測（維生素 D 缺乏症）只有模型分數，沒有試驗或文獻，且疾病詞條已被標為過時。
- 香港仿單的警語與禁忌尚未取得，資料中標為阻擋性缺口，無法進入安全性篩選。

**若要推進需要：**
- 從香港衛生署下載並解析仿單，補齊警語、禁忌與核准適應症（阻擋性缺口）。
- 從 DrugBank 補充作用機轉資料。
- 釐清「obsolete vitamin D deficiency」對應的現行疾病詞條，並重新評估預測。
- 若要優先探索其他方向，建議以**遺傳性低磷佝僂症**作為研究問題：追蹤 NCT03748966 的結果，並確認 NCT03820518 使用的藥物。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


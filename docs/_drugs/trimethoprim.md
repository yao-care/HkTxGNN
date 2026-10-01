---
layout: default
title: Trimethoprim
parent: 僅模型預測 (L5)
nav_order: 895
evidence_level: L5
indication_count: 2
---

# Trimethoprim
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Trimethoprim：從抗菌用藥到點狀上皮角結膜炎

## 一句話總結

Trimethoprim 是細菌二氫葉酸還原酶抑制劑，屬於抗菌藥物，香港已有多張上市許可證。
TxGNN 模型預測它可能對**點狀上皮角結膜炎 (Punctate Epithelial Keratoconjunctivitis)** 有效。
目前針對這個適應症，**沒有任何臨床試驗或文獻**支持，只有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 點狀上皮角結膜炎 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 預測分數 | 99.57%（模型排名 8012） |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 13 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Trimethoprim 抑制細菌的二氫葉酸還原酶，阻斷葉酸合成，因此具有抗菌作用。目前缺乏其他詳細的作用機轉資料。

點狀上皮角結膜炎常由病毒（例如腺病毒）引起，也可能是毒性或免疫介導的反應。抗菌活性對這類病因沒有明確的機轉依據。

TxGNN 給出 99.57% 的高分，是知識圖譜的推論結果，推測是因為它與細菌性結膜炎在圖譜上距離很近。這個分數不等於有臨床或機轉證據。因此，這個預測在機轉上的說服力偏低。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

目前共有 13 張許可證，以下列出 5 張主要許可證。來源資料未提供劑型與核准適應症。

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-56426 | TRIMETHOPRIM SUSP 50MG/5ML | SINO-ASIA PHARMACEUTICAL SUPPLIES LTD |
| HK-43066 | CO-SEPTIC TAB | JEAN-MARIE PHARMACAL CO LTD |
| HK-21138 | SULFAPRIM INJECTABLE SOLN (VET) | WAI LUNG HONG AGRIBUSINESS LTD（獸用） |
| HK-21598 | TRIMETRIN CAP | VICKMANS LABORATORIES LTD |
| HK-09295 | APO-SULFATRIM 400-80MG TAB | HIND WING CO LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個適應症只有模型預測（L5），沒有試驗、文獻或明確的機轉依據。
- 該疾病常為病毒性或免疫性，抗菌藥物的合理性不足。

**補充：排名第 2 的預測「結膜炎」**

這個預測的證據明顯較強（模型分數 99.17%，系統建議為 Proceed with Guardrails）。
但有兩點需要留意：
- 證據等級 L2 的判定偏樂觀。
- 唯一直接相關的試驗是 Phase 4，並非 Phase 3。

| 證據 | 內容 |
|------|------|
| [NCT00581542](https://clinicaltrials.gov/study/NCT00581542) | Phase 4，已完成，124 人。比較 Polytrim（polymyxin B/trimethoprim）眼用液與 moxifloxacin 治療結膜炎。 |
| [PMID 19043945](https://pubmed.ncbi.nlm.nih.gov/19043945/) | 2008 年 RCT。比較 polymyxin B/trimethoprim 與 moxifloxacin 治療細菌性結膜炎的臨床起效速度。 |
| [PMID 30007329](https://pubmed.ncbi.nlm.nih.gov/30007329/) | 2018 年系統性回顧。討論包含 trimethoprim 在內的抗生素治療新生兒披衣菌結膜炎。 |

機轉上只適用於細菌性結膜炎，病毒性、過敏性與披衣菌性結膜炎都不在涵蓋範圍內。這個組合眼用藥看起來更像既有用法，而非真正的老藥新用。

**若要推進需要：**
- 補齊原適應症與核准適應症資料，目前來源中的核准適應症文字全為空白。
- 補充 DrugBank 的作用機轉資料。
- 取得香港衛生署仿單的警語與禁忌資料（目前為阻斷性缺口，無法進入安全性篩選）。
- 針對點狀上皮角結膜炎補做專門文獻檢索，確認是否有病因為細菌的亞群。
- 確認結膜炎使用的路徑（眼用劑型），目前路徑相容性尚未評估。
- 在香港登記系統確認眼用 trimethoprim 複方的上市狀態。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


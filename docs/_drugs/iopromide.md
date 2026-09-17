---
layout: default
title: Iopromide
parent: 僅模型預測 (L5)
nav_order: 408
evidence_level: L5
indication_count: 10
---

# Iopromide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Iopromide：從 X光顯影劑 到 骨關節炎易感性（Osteoarthritis Susceptibility）

## 一句話總結

Iopromide 是非離子型含碘 X 光顯影劑，用於影像診斷顯影，並非治療性藥物，原始適應症資料尚未收集齊全。TxGNN 模型對其列出 10 個候選新適應症，分數最高者為**骨關節炎易感性 (Osteoarthritis Susceptibility)**（99.57%），但**全部 10 個候選皆無臨床試驗支持，機轉上也缺乏合理性**，藥師審核意見一致判定為 Hold。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（已知為含碘 X 光顯影劑，非治療性藥物） |
| 預測新適應症 | 骨關節炎易感性 (Osteoarthritis Susceptibility) |
| TxGNN 預測分數 | 99.57%（rank 8115／全模型） |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測合理？

目前缺乏 Iopromide 的詳細作用機轉（MOA）資料（DG002，High 嚴重度）。根據 Evidence Pack 中各候選適應症的機轉評估，Iopromide 是非離子型含碘 X 光顯影劑，僅用於影像診斷顯影，**沒有已知的抗發炎、軟骨保護、免疫調節或其他治療性藥理作用**。

10 個候選適應症的評估意見一致指出：TxGNN 給出的高分很可能來自知識圖譜中「顯影劑常與骨關節／影像檢查共現」的資料偏差（例如顯影劑常被用於骨關節炎、類風濕性關節炎的影像評估文獻中），而非真實的藥理治療關聯。換言之，**目前沒有機轉證據支持這個預測**，反而其中一則文獻（PMID 16628721）記錄了鐮刀型血球病患者使用低滲透壓靜脈顯影劑後發生腦血管閉塞的不良事件，屬於安全性負面訊號而非治療潛力訊號。

---

## 候選適應症總覽（TxGNN Top 10）

| 排名 | 疾病 | 分數 | 證據等級 | 建議 |
|------|------|------|---------|------|
| 1 | Osteoarthritis susceptibility | 99.57% | L5 | Hold |
| 2 | Osteoarthritis | 99.53% | L5 | Hold |
| 3 | Rheumatoid arthritis | 99.37% | L5 | Hold |
| 4 | Brachyolmia | 99.19% | L5 | Hold |
| 5 | Acromesomelic dysplasia, Hunter-Thompson type | 99.14% | L5 | Hold |
| 6 | Brachyolmia-amelogenesis imperfecta syndrome | 99.12% | L5 | Hold |
| 7 | Alopecia | 99.11% | L5 | Hold |
| 8 | Myosclerosis | 99.09% | L5 | Hold |
| 9 | Hemoglobinopathy | 99.08% | L4（含安全性負面訊號） | Hold |
| 10 | Pseudoachondroplasia | 99.06% | L5 | Hold |

所有候選適應症的推薦決策均為 **Hold**，未有任何一項通過初步機轉合理性檢視。

---

## 臨床試驗證據

目前無相關臨床試驗登記（骨關節炎易感性；其餘 9 個候選適應症亦均無登記試驗）。

---

## 文獻證據

排名第一之「骨關節炎易感性」目前無相關文獻。

以下為其他候選適應症中檢索到的文獻，性質皆為**影像診斷／方法學研究，非治療性研究**：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9678042](https://pubmed.ncbi.nlm.nih.gov/9678042/) | 1998 | Methodology | Clin Orthop Relat Res | MRI 測量關節軟骨體積/厚度之準確性研究（非治療研究） |
| [11419151](https://pubmed.ncbi.nlm.nih.gov/11419151/) | 2001 | Review/Technique | Eur Radiol | CT 導引閉孔神經阻斷術用於髖部疼痛診療（與顯影劑藥理無關） |
| [19435939](https://pubmed.ncbi.nlm.nih.gov/19435939/) | 2009 | Diagnostic imaging | Radiology | 顯影增強 CT 用於類風濕性關節炎滑膜炎影像評估（診斷用途） |
| [16628721](https://pubmed.ncbi.nlm.nih.gov/16628721/) | 2006 | Case report (adverse event) | Am J Hematol | 鐮刀型血球病患者使用低滲透壓靜脈顯影劑後發生腦血管閉塞事件（**安全性負面訊號**） |
| [9094239](https://pubmed.ncbi.nlm.nih.gov/9094239/) | 1997 | Case report | Pediatr Radiol | Noonan 氏症候群新生兒淋巴管攝影檢查病例報告（診斷用途） |

---

## 安全性考量

安全性資訊請參考原廠仿單。TFDA 仿單警語與禁忌症資料尚未取得（DG001，**Blocking** 嚴重度），目前無法進行 S1 安全性初評。

---

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 排名前 10 的候選適應症證據等級均僅為 L5（一項為 L4），無任何臨床試驗支持；文獻多屬影像診斷/方法學性質，且機轉評估一致認為缺乏合理藥理基礎。
- 香港未上市（0 張許可證），且 TFDA 仿單警語/禁忌資料缺失（DG001，Blocking），無法完成安全性初評，即使未來出現效果訊號也無法立即推進。

**若要推進需要：**
- 補齊 TFDA/藥監局仿單警語與禁忌症資料（DG001）
- 補齊 Iopromide 詳細作用機轉資料（DG002）
- 若日後出現機轉合理的新證據（如動物實驗或病例對照研究），需重新評估是否有進一步收集證據之必要
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


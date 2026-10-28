---
layout: default
title: Pyrazinamide
parent: 僅模型預測 (L5)
nav_order: 747
evidence_level: L5
indication_count: 10
monitor_inn: "PYRAZINAMIDE"
predicted_indications: ["infectious otitis media", "middle ear disease", "otosalpingitis", "chronic otitis media", "suppurative otitis media", "non-suppurative otitis media", "middle ear cholesterol granuloma", "allergic otitis media", "Lyme disease", "infectious otitis interna"]
last_modified_at: 2026-10-28
description: "Pyrazinamide：預測新適應症為感染性中耳炎 (Infectious Otitis Media)（證據等級 L5）。原適應症：肺結核、結核性腦膜炎"
---

# Pyrazinamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Pyrazinamide：從結核病到感染性中耳炎
{: .text-alpha }

## 一句話總結

Pyrazinamide（吡嗪醯胺）是抗結核藥物，知識圖譜記錄的使用方向為肺結核與結核性腦膜炎。
TxGNN 模型預測它可能對**感染性中耳炎 (Infectious Otitis Media)** 有效，但目前**沒有臨床試驗和文獻**直接支持這個預測。
僅有的相關文獻是結核性中耳炎的個案報告，屬於結核病本身的治療，並非真正的新適應症。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肺結核、結核性腦膜炎（知識圖譜記錄的關係；香港許可證未載明適應症文字） |
| 預測新適應症 | 感染性中耳炎 (Infectious Otitis Media) |
| TxGNN 預測分數 | 0.9996 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Pyrazinamide 是一種前驅藥，在酸性環境下會轉變為活性型態 pyrazinoic acid，只對結核分枝桿菌 (*Mycobacterium tuberculosis*) 有活性。

一般感染性中耳炎的常見致病菌為肺炎鏈球菌、流感嗜血桿菌與卡他莫拉菌，Pyrazinamide 對這些細菌沒有已知活性。因此，這個高分預測缺乏機轉上的支持。分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，不是生物學證據。

唯一合理的情境是罕見的結核性中耳炎，此時 Pyrazinamide 作為標準抗結核複方的一部分使用，屬於原適應症（結核病）在肺外部位的延伸，而非真正的藥物再利用。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

針對「感染性中耳炎」本身，目前無相關文獻。

以下為相鄰疾病（中耳疾病、慢性／化膿性中耳炎）的文獻，均為個案報告，且皆指向結核性中耳炎，並非直接研究感染性中耳炎：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26785789](https://pubmed.ncbi.nlm.nih.gov/26785789/) | 2013 | Case report | Int J Mycobacteriol | 55 歲女性鼻腔與中耳結核，以 rifampicin、isoniazid、pyrazinamide 治療 9 個月，追蹤一年無復發 |
| [15168420](https://pubmed.ncbi.nlm.nih.gov/15168420/) | 2004 | Case report | Am J Kidney Dis | 腎臟移植受贈者的結核性中耳炎，先前多次經驗性抗生素治療無效 |
| [41783873](https://pubmed.ncbi.nlm.nih.gov/41783873/) | 2026 | Case report | Cureus | 結核性中耳炎表現隱匿，常延遲診斷 |
| [8011030](https://pubmed.ncbi.nlm.nih.gov/8011030/) | 1994 | Case report | Laryngo- rhino- otologie | 12 例頭頸部結核，其中 1 例位於中耳 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-34750 | PYRAFAT TAB 500MG | 未載明 | 未載明 |
| HK-06490 | PYRAZINAMIDE TAB 500MG | 未載明 | 未載明 |
| HK-26892 | RIFATER TAB | 未載明 | 未載明 |

## 安全性考量

- **知識圖譜記錄的禁忌關係**（非仿單內容）：肝衰竭、急性肝衰竭、肝病、肝炎、紫質症（含遺傳性紫質症、紫質代謝疾病）、膽囊疾病、糖尿病、糖尿病酮酸中毒、痛風、周邊神經系統疾病、周邊神經病變、物質濫用／依賴、慢乙醯化型。
- **藥物交互作用**：共查得 56 筆，以下為部分項目。
  - 中度：Picosulfuric acid、Naltrexone
  - 其他（嚴重程度未定）：Pantoprazole、Omeprazole、Lansoprazole、Prednisone、Prednisolone、Amphotericin B、Streptomycin、Metronidazole、Glyburide、Acetylsalicylic acid 等

詳細警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 針對感染性中耳炎沒有任何臨床試驗或直接研究，Pyrazinamide 對一般中耳炎致病菌也無已知活性，因此證據等級為 L5。
- 現有文獻僅涉及結核性中耳炎，屬於原抗結核適應症的延伸，不能支持對一般感染性中耳炎的再利用。

**若要推進需要：**
- 補充 Pyrazinamide 的作用機轉資料
- 取得香港仿單的警語、禁忌與核准適應症文字
- 體外試驗確認對中耳炎常見致病菌是否有活性，以及中耳組織的藥物穿透性
- 若聚焦結核性中耳炎，則應視為原適應症的肺外延伸，另行評估，而非再利用案例

**其他預測的補充說明：**排名前 10 的預測中，多數為耳部疾病，且皆無試驗支持。「萊姆病」雖有間接的假說性訊號（針對休眠菌的概念），但檢索到的文獻是 dapsone 複方與一般性回顧，並非 Pyrazinamide 專屬的臨床證據，僅可視為研究問題。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


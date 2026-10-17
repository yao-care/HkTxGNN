---
layout: default
title: Paliperidone
parent: 僅模型預測 (L5)
nav_order: 658
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Paliperidone：預測新適應症為視網膜失養症（伴或不伴眼外異常）（證據等級 L5）。原適應症：精神病性疾患、類思覺失調症、思覺失調症、情感性思覺失調症、精神疾患"
monitor_inn: "PALIPERIDONE"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "myopia X-linked", "syndromic myopia", "hydranencephaly (disease)", "congenital disorder of glycosylation with defective fucosylation"]
---

# Paliperidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Paliperidone：從思覺失調症到視網膜失養症（預測）

## 一句話總結

Paliperidone 是一種非典型抗精神病藥，原本用於精神病性疾患、思覺失調症、情感性思覺失調症等精神疾病。
TxGNN 模型預測它可能對**視網膜失養症（retinal dystrophy with or without extraocular anomalies）**有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅是模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 精神病性疾患、類思覺失調症、思覺失調症、情感性思覺失調症、精神疾患（許可證資料中未提供適應症文字，此處依知識圖譜的適應症資料） |
| 預測新適應症 | 視網膜失養症（伴或不伴眼外異常） |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知資訊，Paliperidone 是多巴胺 D2 與血清素 5-HT2A 受體拮抗劑，其在精神分裂症等精神疾病的療效已被證實。

然而，視網膜失養症多為單基因的結構或退化性疾病，病變位於光受體或視網膜色素上皮。目前沒有已知途徑顯示多巴胺或血清素拮抗作用可以改變這類疾病的進程。

因此，**機轉上看不出明確關聯**。0.999 的高分很可能反映知識圖譜中的鄰近關係（例如共同的基因或表型），而非藥理學上的理由，應視為待驗證的假說。

同一份預測名單中的其他項目（X 連鎖近視、症候群性近視、無腦回腦積水、岩藻糖基化缺陷的先天性糖基化異常）同樣沒有試驗或文獻支持，也缺乏合理的機轉連結。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 20 張有效單方許可證，無已註銷者。主要許可證如下（資料中未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-56192 | INVEGA EXTENDED-RELEASE TAB 3MG | Johnson & Johnson (Hong Kong) |
| HK-60141 | INVEGA SUSTENNA 肌肉注射長效懸液 50MG | Johnson & Johnson (Hong Kong) |
| HK-64970 | INVEGA TRINZA 長效注射懸液 175MG | Johnson & Johnson (Hong Kong) |
| HK-68020 | INVEGA HAFYERA 預充填注射 1000MG/5ML | Johnson & Johnson (Hong Kong) |
| HK-68512 | COMPASSIA 長效注射懸液 50MG/0.5ML | Abbott Lab |

其餘許可證包括 Pamoprex（Sino Pacific）、Paliperidone 緩釋錠（Hong Kong Medical Supplies、I & C）以及 Paliperidone Teva 注射劑等。

---

## 安全性考量

- **禁忌症（知識圖譜資料，非仿單內容）**：圖譜中與本藥有禁忌關聯的疾病包括：
  - 心血管：長 QT 症候群、尖端扭轉型心室頻脈、姿勢性低血壓、姿勢性心搏過速症候群、心肌梗塞
  - 神經：癲癇、基底核疾病、眼瞼痙攣
  - 代謝：糖尿病、糖尿病酮酸中毒、高血糖、高脂血症、肥胖
  - 血液：嗜中性白血球低下、顆粒球缺乏症
  - 腸胃：克隆氏症、發炎性腸道疾病
  - 其他：缺鉀症、腎功能不全、乳癌
- **藥物交互作用**：資料庫查得 100 筆交互作用，以下為部分範例。
  - 嚴重（Major）：Bupropion、Morphine
  - 中度（Moderate）：降血糖藥（Metformin、Pioglitazone、Acarbose、Alogliptin、Canagliflozin、Chlorpropamide、Albiglutide）、抗膽鹼藥（Atropine、Hyoscyamine、Glycopyrronium）、Famotidine、Epinephrine、Hydrocortisone、Amphotericin B、Loperamide、Lorcaserin、Bisacodyl

仿單的警語與禁忌資料尚未取得，完整安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測完全依賴模型分數，沒有臨床試驗或文獻，證據等級為 L5。
- 機轉上沒有合理的關聯，且該藥的禁忌與交互作用不少，不建議投入開發資源。

**若要推進需要：**
- 取得 Paliperidone 完整的作用機轉資料。
- 以文獻回顧確認視網膜中多巴胺／血清素訊號與該類疾病是否有關，並進行前臨床驗證。
- 取得香港仿單的警語與禁忌資料，進行安全性評估。
- 檢視 TxGNN 高分是否來自知識圖譜中的人為關聯。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


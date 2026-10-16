---
layout: default
title: Tramadol
parent: 僅模型預測 (L5)
nav_order: 893
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tramadol：預測新適應症為肢中段發育不良 Hunter-Thompson 型 (Acromesomelic Dysplasia…（證據等級 L5）。原適應症：骨關節炎 (osteoarthritis)、關節病變 (arthropathy)"
---

# Tramadol
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

# Tramadol：從骨關節炎到先天性骨骼發育不良（Hunter-Thompson 型肢中段發育不良）

## 一句話總結

Tramadol 是一種鴉片類止痛藥，原本用於骨關節炎與關節病變相關的疼痛。
TxGNN 模型預測它可能對**肢中段發育不良 Hunter-Thompson 型 (Acromesomelic Dysplasia, Hunter-Thompson Type)** 有效，
但目前**沒有任何臨床試驗或直接文獻**支持，這個預測僅來自知識圖譜的計算推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 骨關節炎 (osteoarthritis)、關節病變 (arthropathy) |
| 預測新適應症 | 肢中段發育不良 Hunter-Thompson 型 (Acromesomelic Dysplasia, Hunter-Thompson Type) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Tramadol 是 mu 型鴉片受體促效劑，同時抑制血清素與正腎上腺素的再攝取，可提供症狀性的止痛效果。

模型給出高分，可能是因為 Tramadol 在知識圖譜中與骨關節炎、關節病變相連，而這些疾病與骨骼、關節疾病在網路結構上有許多共同鄰居。這是圖譜關聯，並非生物學上的證據。

Hunter-Thompson 型肢中段發育不良是一種遺傳性骨骼發育疾病，與 GDF5/CDMP1 訊號異常有關。Tramadol 對這條路徑沒有已知作用，最多只能緩解疼痛，不能改變疾病本身。

其他排名前 10 的預測（如短軀幹症、假性軟骨發育不全、幼年型特發性關節炎等）情況類似，同樣沒有機轉連結或直接證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

（排名第 7 的「幼年型特發性關節炎」預測雖有 1 篇文獻，但內容是 ketoprofen 在兒童的研究，並非 Tramadol，不能作為本藥的直接證據。）

---

## 香港上市資訊

香港共有 20 張有效的單一成分許可證，皆為已上市狀態。以下列出 5 張代表性許可證，資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-58224 | TRADOLGESIC CAP 50MG | 膠囊（依品名） | 無資料 |
| HK-66387 | MYOTRAM 100 SOLUTION FOR INJECTION/INFUSION 100MG/2ML | 注射／輸注液（依品名） | 無資料 |
| HK-35707 | MABRON CAP 50MG | 膠囊（依品名） | 無資料 |
| HK-44533 | SEFMAL CAP 50MG | 膠囊（依品名） | 無資料 |
| HK-41704 | TRAMADOL 50 STADA CAP 50MG | 膠囊（依品名） | 無資料 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自圖譜關聯，並非仿單內容）：高血壓、癲癇、肝衰竭、肝病、肝硬化、糖尿病酮酸中毒、呼吸衰竭、物質濫用／依賴、酒精戒斷、血清素症候群、顱內高壓、對乙醯胺酚中毒、中樞神經系統感染等。
- **藥物交互作用**：共查得 100 筆，以下為部分重要項目。
  - 嚴重 (Major)：Alvimopan、Bupropion、Cisapride、Dexfenfluramine、Diethylpropion、Dolasetron、Dronabinol、Ephedrine、Fenfluramine
  - 中度 (Moderate)：Atropine、Bisacodyl、Cimetidine、Clarithromycin、Famotidine 等

香港仿單的警語與禁忌資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測完全來自圖譜計算，沒有臨床試驗、直接文獻或機轉連結支持（證據等級 L5）。
- Tramadol 只能症狀性止痛，無法改變此類遺傳性骨骼發育疾病的病程。
- 兒童使用鴉片類藥物另有安全疑慮。

**若要推進需要：**
- 取得香港仿單的警語與禁忌資料，完成基本安全性篩選。
- 補齊 Tramadol 的作用機轉資料。
- 若考慮疼痛管理用途，應另行評估 Tramadol 對這些罕見骨骼疾病的症狀緩解證據，而不是以疾病治療為目標。
- 在沒有新的直接證據前，不建議投入進一步開發資源。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


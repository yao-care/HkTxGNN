---
layout: default
title: Celecoxib
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Celecoxib：預測新適應症為肢端中段發育不良，Hunter-Thompson 型 (Acromesomelic dysplasia…（證據等級 L5）。原適應症：類風濕性關節炎、僵直性脊椎炎、骨關節炎、幼年型特發性關節炎等"
monitor_inn: "CELECOXIB"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "rheumatoid nodulosis", "inflammatory spondylopathy", "WHIM syndrome"]
---

# Celecoxib
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

# Celecoxib：從類風濕性關節炎到肢端中段發育不良（Hunter-Thompson 型）

## 一句話總結

Celecoxib 是選擇性 COX-2 抑制劑，原本用於類風濕性關節炎、僵直性脊椎炎、骨關節炎等關節發炎疾病。
TxGNN 模型預測它可能對**肢端中段發育不良，Hunter-Thompson 型 (Acromesomelic dysplasia, Hunter-Thompson type)** 有效。
目前**沒有任何臨床試驗或文獻**支持這個預測，且機轉上缺乏合理連結，僅屬模型推測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 類風濕性關節炎、僵直性脊椎炎、骨關節炎、幼年型特發性關節炎等（來自知識圖譜；香港許可證資料未提供適應症文字） |
| 預測新適應症 | 肢端中段發育不良，Hunter-Thompson 型 (Acromesomelic dysplasia, Hunter-Thompson type) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Celecoxib 屬於 COX-2 選擇性 NSAID，透過抑制前列腺素合成來減輕發炎與疼痛，在關節炎相關疾病中的療效已被證實。

然而，Hunter-Thompson 型肢端中段發育不良是罕見的遺傳性骨骼發育異常，成因為 CDMP1/GDF5 功能喪失，屬於結構性的發育缺陷。COX-2 抑制只能緩解發炎，不預期能矯正這類先天性骨骼發育問題。

因此，**我們判斷這個預測缺乏可信的機轉連結**。99.88% 的高分只是圖譜演算法的結果，不等於有生物學或臨床上的支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Celecoxib 在香港共有 20 張有效許可證，皆為單一成分製劑，無已註銷者。以下列出 5 張主要許可證：

| 許可證號 | 品名 | 廠商 | 規格 |
|---------|------|------|------|
| HK-44731 | CELEBREX CAP 200MG | VIATRIS HEALTHCARE HONG KONG LIMITED | 200 mg |
| HK-61703 | CELECOXIB SANDOZ CAPSULES 200MG | SANDOZ HONG KONG LIMITED | 200 mg |
| HK-61704 | CELECOXIB SANDOZ CAPSULES 100MG | SANDOZ HONG KONG LIMITED | 100 mg |
| HK-67377 | HOVID CELECOXIB CAPSULES 200MG | HOVID LIMITED | 200 mg |
| HK-64176 | APO-CELECOXIB CAPSULES 100MG | HIND WING CO LTD | 100 mg |

---

## 安全性考量

- **知識圖譜標示的禁忌或需謹慎疾病**（來自圖譜推論，非仿單原文）：
  - 心血管：高血壓、充血性心衰竭、心肌梗塞、中風與腦血管疾病
  - 腎臟、肝臟、膽囊疾病
  - 消化性潰瘍（含活動性潰瘍）
  - 氣喘（含過敏性、內因性）
  - 貧血與血紅蛋白病變
  - 物質濫用或依賴
- **藥物交互作用**：資料庫共查得 100 筆。
  - 嚴重（Major）：Eliglustat
  - 中度（Moderate）：Hydrocortisone、Metformin、Cimetidine、Levofloxacin、Metronidazole、Naltrexone，以及多種降血糖藥（Glimepiride、Glipizide、Glyburide、Chlorpropamide、Acetohexamide、Nateglinide、Exenatide）和水楊酸類藥物（Mesalazine、Balsalazide、Olsalazine）等

完整警語與禁忌請以原廠仿單為準。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 此適應症為罕見遺傳性骨骼發育疾病，COX-2 抑制無法作用於其病因。
- 沒有任何臨床試驗或文獻，證據等級僅 L5，高預測分數不足以支持推進。

**若要推進需要：**
- 找出 GDF5/CDMP1 訊號路徑與前列腺素或 COX-2 路徑之間是否存在任何生物學關聯
- 前臨床模型（細胞或動物）的初步佐證
- 完整的作用機轉資料與香港仿單的警語、禁忌資料

**補充：** 同一批預測中，「發炎性脊椎病變 (inflammatory spondylopathy)」對應僵直性脊椎炎，已有多個已完成的 Phase 3/4 隨機試驗支持。但那屬於原有適應症的確認，並非新的藥物再利用。若要尋找實質再利用機會，建議另行評估其他預測。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


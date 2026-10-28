---
layout: default
title: Gefitinib
parent: 僅模型預測 (L5)
nav_order: 410
evidence_level: L5
indication_count: 9
monitor_inn: "GEFITINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "lung benign neoplasm", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "lung germ cell tumor", "pulmonary sulcus neoplasm", "junctional epidermolysis bullosa"]
last_modified_at: 2026-10-23
description: "Gefitinib：預測新適應症為牙齦纖維瘤病 (Fibromatosis, Gingival)（證據等級 L5）。原適應症：非小細胞肺癌、肺癌"
---

# Gefitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Gefitinib：從非小細胞肺癌到牙齦纖維瘤病
{: .text-alpha }

## 一句話總結

Gefitinib 是一種 EGFR 酪胺酸激酶抑制劑，知識圖譜記錄其原適應症為非小細胞肺癌與肺癌。
TxGNN 模型預測它可能對 **牙齦纖維瘤病 (Fibromatosis, Gingival)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 非小細胞肺癌、肺癌（知識圖譜記錄；本報告彙整的香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 牙齦纖維瘤病 (Fibromatosis, Gingival) |
| TxGNN 預測分數 | 0.9989 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 11 張／共 11 張） |
| 許可證數 | 11 張（有效 11 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，gefitinib 是 EGFR 酪胺酸激酶抑制劑，在肺癌（尤其是帶有 EGFR 突變者）中的用途已有大量文獻討論，機轉上可能透過 EGFR/ErbB 訊號影響纖維母細胞增生，這是一個合理但**尚未被驗證**的假說。

牙齦纖維瘤病是牙齦結締組織過度增生的疾病。目前沒有資料顯示 EGFR 抑制可改善此病，TxGNN 的高分（0.9989）來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，不是生物學證據，不能視為臨床證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 11 張有效的單方 gefitinib 許可證（250 mg 錠劑），本次彙整資料未載明劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-51753 | IRESSA TAB 250MG | ASTRAZENECA HONG KONG LIMITED |
| HK-66380 | VEIASU TABLETS 250MG | LOTUS PHARMACEUTICAL HK LIMITED |
| HK-66418 | GERITSA TABLETS 250MG | JACOBSON MARKETING LIMITED |
| HK-66918 | APO-GEFITINIB TABLETS 250MG | HIND WING CO LTD |
| HK-66963 | GEFITINIB SANDOZ TABLETS 250MG | SANDOZ HONG KONG LIMITED |

（另有 6 張許可證未在此列出。）

---

## 細胞毒性

gefitinib 屬標靶藥物（EGFR 酪胺酸激酶抑制劑），並非傳統細胞毒性化療藥物。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（EGFR-TKI） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 肝功能（文獻有嚴重肝毒性報告）、肺部症狀（間質性肺病風險） |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單文字）**：肝病、膽囊疾病、間質性肺病、肺纖維化、發炎後肺纖維化。
- **藥物交互作用**：共查得 100 筆，以下為中等等級的主要項目：
  - 胃酸抑制劑：famotidine、ranitidine、cimetidine、nizatidine，以及 omeprazole、esomeprazole、pantoprazole、lansoprazole、rabeprazole、dexlansoprazole 等氫離子幫浦抑制劑
  - 其他：clarithromycin、aprepitant、dexamethasone、naltrexone、miconazole、clotrimazole、troglitazone
- **相關文獻提示的風險**：間質性肺病、急性肺炎、嚴重肝毒性、皮膚毒性、QT 延長，其中皮膚毒性對皮膚脆弱類疾病需特別留意。

其他警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 針對牙齦纖維瘤病，沒有任何臨床試驗或文獻，證據等級為 L5，僅有模型預測。
- gefitinib 有間質性肺病與肝毒性等嚴重風險，在缺乏療效證據下不宜推進。

**若要推進需要：**
- 補充 EGFR/ErbB 訊號與牙齦纖維母細胞增生關聯的機轉研究
- 取得 gefitinib 的作用機轉資料與香港仿單的警語、禁忌
- 先以細胞或動物模型做概念驗證，再評估是否有必要進入臨床研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


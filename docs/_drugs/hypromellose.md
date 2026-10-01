---
layout: default
title: Hypromellose
parent: 僅模型預測 (L5)
nav_order: 442
evidence_level: L5
indication_count: 10
---

# Hypromellose
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

# Hypromellose：從眼用潤滑劑到肝靜脈阻塞性疾病併免疫缺陷症候群

## 一句話總結

Hypromellose（羥丙甲纖維素）是纖維素醚類成分，在香港以人工淚液等眼藥水形式上市。
TxGNN 模型預測它可能對**肝靜脈阻塞性疾病併免疫缺陷症候群 (Hepatic veno-occlusive disease-immunodeficiency syndrome)** 有效。
目前**沒有臨床試驗**，也**沒有文獻**支持這個預測，屬於純模型輸出。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 肝靜脈阻塞性疾病併免疫缺陷症候群 (Hepatic veno-occlusive disease-immunodeficiency syndrome) |
| TxGNN 預測分數 | 98.30% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Hypromellose 是一種纖維素醚類成分，主要作為眼用潤滑劑的活性成分，或在各類製劑中作為賦形劑（增稠、成膜、保濕）。它本身沒有已知的藥理作用機轉。

原本的用途（眼睛表面潤滑）與預測的新適應症（一種伴隨免疫缺陷的罕見肝血管疾病）在生物學上沒有明顯關聯。Hypromellose 對肝竇內皮細胞或此疾病的病理生理沒有已知作用。

因此，0.983 的高分很可能是知識圖譜結構造成的假象，而不是真實的生物訊號。這個預測**目前不具備合理的機轉支持**。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

目前無相關文獻

---

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張主要許可證：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-46636 | GENTEAL LUBRICANT EYE DROPS 0.3% | ALCON HONG KONG LTD |
| HK-64590 | LOSTEAR EYE DROPS 0.3% W/V | EUROPHARM LAB CO LTD |
| HK-45257 | LAC-OPH EYE DROPS 0.5% | HEALTH ALLIANCE INTERNATIONAL CO LTD |
| HK-67786 | HIPRO EYE DROPS 0.3% W/V | CHEMILL PHARMA LIMITED |
| HK-22087 | HYPROMELLOSE EYE DROPS 0.3% | THE INTERNATIONAL MEDICAL COMPANY LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數，沒有任何臨床試驗或文獻佐證（L5）。Hypromellose 也沒有已知的藥理活性與此疾病相關，高分很可能是知識圖譜的假象。
- 其他排名前 10 的預測同樣沒有機轉支持。排名第 8 的乾癬有 1 項登記試驗，但該試驗測試的是口服補充品，與 Hypromellose 無關，不能作為佐證。

**若要推進需要：**
- 補齊 Hypromellose 的作用機轉資料（例如查詢 DrugBank），確認是否有任何藥理活性。
- 取得香港衛生署的仿單，補齊警語與禁忌資料。
- 找出模型給出此預測的知識圖譜路徑，判斷是否為資料假象。
- 除非出現新的生物學或臨床證據，否則不建議投入資源。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


---
layout: default
title: Gilteritinib
parent: 僅模型預測 (L5)
nav_order: 346
evidence_level: L5
indication_count: 1
---

# Gilteritinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Gilteritinib：從急性骨髓性白血病到延髓型脊髓灰質炎

## 一句話總結

Gilteritinib 是 FLT3/AXL 雙重酪胺酸激酶抑制劑，核准用於 FLT3 突變型急性骨髓性白血病（AML）治療。
TxGNN 模型預測它可能對**延髓型脊髓灰質炎（Bulbar Polio）** 有效，
然而目前**無任何臨床試驗或文獻**支持，屬於純計算推測，機轉連結極為薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | FLT3 突變型急性骨髓性白血病（AML） |
| 預測新適應症 | 延髓型脊髓灰質炎（Bulbar Polio） |
| TxGNN 預測分數 | 99.10% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Gilteritinib 是 FLT3（FMS 樣酪胺酸激酶 3）與 AXL 的雙重抑制劑，透過阻斷突變 FLT3 驅動的異常細胞增殖信號，用於治療 FLT3 突變型 AML。

延髓型脊髓灰質炎（Bulbar Polio）是小兒麻痺病毒（Poliovirus，屬 Picornaviridae 科）感染腦幹延髓所引起的嚴重病症，病毒經由 CD155（PVR）受體進入細胞，與 FLT3 或 AXL 信號軸並無已知的直接關聯。

雖然 AXL 在 Zika、Dengue、Ebola 等病毒的 TAM 受體橋接入侵機制中有所描述（透過 Gas6/Protein S 橋接），但 Poliovirus 並不利用此路徑。**兩個適應症在疾病類型（血液腫瘤 vs. 病毒性神經感染）、靶點、病理機轉上均無實質交集，機轉連結極為薄弱，此預測屬於純計算模型的假設輸出，不具直接可信度。**

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（FLT3/AXL 酪胺酸激酶抑制劑） |
| 骨髓抑制風險 | 中至高度（貧血、嗜中性白血球減少、血小板減少為已知常見不良反應） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含分類計數）、肝腎功能、QTc 間期、電解質（尤其磷酸鹽）、澱粉酶/脂肪酶 |
| 處置防護 | 請依細胞毒性藥物處置規範操作 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
Gilteritinib 與延髓型脊髓灰質炎之間缺乏可信的機轉連結，目前無任何臨床試驗或文獻佐證，僅有計算模型預測（L5 等級），且 Poliovirus 的感染路徑與 FLT3/AXL 信號軸無關，再利用的生物學合理性不足。

**若要推進需要：**
- 完整的作用機轉資料（MOA），確認 Gilteritinib 是否有任何抗病毒活性的基礎研究
- 體外（in vitro）AXL 抑制對 Poliovirus 感染的功能驗證實驗
- 取得台灣 TFDA 仿單，補齊警語與禁忌症資料（現為 Blocking 缺口）
- 重新評估是否有其他 AXL 抑制劑在腸病毒/小 RNA 病毒領域已有前臨床數據，作為類推依據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Fluorometholone
parent: 中證據等級 (L3-L4)
nav_order: 327
evidence_level: L3
indication_count: 5
---

# Fluorometholone
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

# Fluorometholone：從眼科局部消炎到細菌感染後眼部疾病

## 一句話總結

Fluorometholone 是一種眼科局部用糖皮質素，主要用於控制眼表炎症反應。TxGNN 模型預測它可能對**細菌感染後疾病 (Post-bacterial Disorder)** 有效，目前有 **2 個臨床試驗**直接測試此治療方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 眼科局部炎症治療（糖皮質素眼藥水） |
| 預測新適應症 | 細菌感染後疾病 (Post-bacterial Disorder) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏完整的作用機轉資料。根據臨床研究背景資訊，Fluorometholone 屬於合成糖皮質素類眼科製劑，設計用於局部眼表使用，具有良好的角膜穿透性，且相較於 prednisolone 引發眼壓升高的風險較低。糖皮質素類藥物通過抑制磷脂酶 A2 活性、下調 IL-1β、IL-6、TNF-α 等促炎細胞因子來發揮廣泛的抗炎效果。

細菌感染後疾病（Post-bacterial Disorder）在眼科場景中的典型表現包括：細菌性角膜潰瘍恢復期（病原體清除後的持續角膜炎症）及沙眼（Chlamydia trachomatis 細菌性感染）引起的後遺性眼瞼內翻。兩者共同的病理機轉均為感染控制後殘留炎症持續造成組織損傷與瘢痕形成，fluorometholone 的抗炎特性恰好可在此時介入，減少後遺炎症損傷、保護視力功能。

兩項已識別的臨床試驗均在完整抗生素覆蓋下使用 fluorometholone，體現了「先控感染、後抗炎」的核心安全原則，亦反映研究者認為此藥有足夠的前期依據值得進一步探索。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07308938](https://clinicaltrials.gov/study/NCT07308938) | Phase 2 | 尚未招募 | 174 | 評估局部 fluorometholone 作為細菌性角膜潰瘍標準抗生素治療外的輔助療法，主要終點為 3 個月最佳矯正視力（BCVA） |
| [NCT01949454](https://clinicaltrials.gov/study/NCT01949454) | N/A | 已完成 | 154 | 沙眼性眼瞼內翻（倒睫）手術後使用 fluorometholone 0.1% 圍術期輔助抗炎治療，評估是否可降低術後復發性倒睫風險及瘢痕形成 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 其他 TxGNN 預測一覽

除主要預測（Post-bacterial Disorder）外，TxGNN 對 Fluorometholone 尚有以下 4 項預測，分數相近但證據基礎差異明顯：

| 排名 | 適應症 | 預測分數 | 證據等級 | 建議 | 備注 |
|------|--------|---------|---------|------|------|
| 1 | 感染後血管炎 (Postinfectious Vasculitis) | 99.91% | L5 | Hold | 機轉合理但系統性給藥路徑不明，眼科局部製劑不適用 |
| 3 | 外耳炎 (Otitis Externa) | 99.90% | L5 | Hold | 劑型為眼用製劑，耳用可行性未知；鼓膜穿孔時有安全疑慮 |
| 4 | 感染性尿道狹窄 (Infective Urethral Stricture) | 99.90% | L5 | Hold | 需系統給藥，眼科局部製劑無法達到目標部位；可能為 KG 過度泛化 |
| 5 | 感染後綜合症 (Post-infectious Syndrome) | 99.90% | L4 | Research Question | 有一項間接相關的 Phase 4 試驗（NCT05771194，術後眼表干預，40 人），屬早期訊號 |

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
2 項臨床試驗直接測試 fluorometholone 在細菌感染後眼科疾病的應用，其中 NCT01949454（沙眼相關眼瞼內翻，154 人）已完成，提供初步可行性與安全性依據；Phase 2 試驗 NCT07308938（細菌性角膜潰瘍，174 人）目前處於招募前階段，顯示研究者對此方向具有足夠信心進行進一步評估。

**若要推進需要：**
- 補充完整 MOA 資料（DrugBank API 查詢 DB00324）
- 取得安全性仿單資訊（香港衛生署許可仿單或原廠說明書警語、禁忌症）
- 評估劑型與給藥路徑相容性：Fluorometholone 現有劑型為眼用製劑，若未來考慮擴展至外耳炎等其他感染後適應症，需先確認劑型適配性
- 持續追蹤 NCT07308938 的招募進展與 Phase 2 結果，該試驗將提供迄今最直接的療效證據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


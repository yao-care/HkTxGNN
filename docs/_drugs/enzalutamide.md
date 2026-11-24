---
layout: default
title: Enzalutamide
parent: 僅模型預測 (L5)
nav_order: 325
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
monitor_inn: "ENZALUTAMIDE"
predicted_indications: ["prostate leiomyoma", "Brenner tumor", "fibroma of prostate", "benign reproductive system neoplasm", "benign prostate phyllodes tumor"]
description: "Enzalutamide：預測新適應症為Prostate leiomyoma（證據等級 L5）。香港藥劑製品註冊：4 張（有效 4 張）"
---

# Enzalutamide
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

## Enzalutamide: Prostate leiomyoma
{: .text-alpha }

## 一句話總結

Enzalutamide 是雄性素受體（AR）抑制劑，原本用於治療攝護腺癌。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Prostate leiomyoma |
| TxGNN 預測分數 | 0.9957 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Enzalutamide 是 AR 抑制劑，作用包括阻斷雄性素與受體結合、抑制受體進入細胞核，以及阻止受體與 DNA 結合。根據美國 FDA 核准的 Enzalutamide 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Enzalutamide 是一種雄激素受體抑制劑，作用於雄激素受體訊息傳遞路徑中的不同步驟。Enzalutamide 已被證實可競爭性抑制雄激素與雄激素受體的結合；並因此抑制雄激素受體的核轉位及其與 DNA 的交互作用。」英文原文："Enzalutamide is an androgen receptor inhibitor that acts on different steps in the androgen receptor signaling pathway. Enzalutamide has been shown to competitively inhibit androgen binding to androgen receptors; and consequently, inhibits nuclear translocation of androgen receptors and their interaction with DNA."（[DailyMed: Xtandi (enzalutamide) prescribing information, Astellas Pharma US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b129fdc9-1d8e-425c-a5a9-8a2ed36dfbdf)，版本日期 2026-07-28；查閱日期 2026-11-19）。

「攝護腺癌／腦癌易感性」是遺傳性癌症易感性的分類，描述的是體質傾向，不是可直接用藥治療的疾病狀態。因此，模型的高分更像是反映疾病分類上的接近，不代表有新的療效訊號。

目前沒有試驗或文獻檢驗 enzalutamide 在這個分類上的作用，預測在臨床上暫時無法採取行動。

**補充說明：**其他預測的適應症也都缺乏直接證據。
- 「男性生殖器官癌症」雖有較多試驗與文獻，但內容主要是攝護腺癌，也就是原有適應症，不算新的再利用機會。
- 攝護腺平滑肌瘤、攝護腺纖維瘤、良性攝護腺葉狀腫瘤等罕見良性腫瘤，目前只有 AR 訊號傳導的理論推測，沒有試驗或文獻。
- Brenner 瘤沒有明確的雄性素受體依賴性，預測可能只是反映疾病分類上的接近。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-63493 | XTANDI CAPSULES 40MG | 單一成分 | ASTELLAS PHARMA HONG KONG COMPANY LIMITED | 有效 |
| HK-68829 | XTANDI FILM-COATED TABLETS 40MG | 單一成分 | ASTELLAS PHARMA HONG KONG COMPANY LIMITED | 有效 |
| HK-68830 | XTANDI FILM-COATED TABLETS 80MG | 單一成分 | ASTELLAS PHARMA HONG KONG COMPANY LIMITED | 有效 |
| HK-68934 | ENZACORD 40 CAPSULES 40MG | 單一成分 | JACOBSON MARKETING LIMITED | 有效 |

<!-- licenses:end -->

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶／荷爾蒙治療藥物（AR 抑制劑），非傳統細胞毒性化療 |

骨髓抑制風險、致吐性分級、監測項目與處置防護，請參考原廠仿單的警語與注意事項。

---

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用紀錄，以下為其中部分。
  - **嚴重 (Major)**：Bupropion、Dolasetron、Eliglustat
  - **中度 (Moderate)**：Famotidine、Rabeprazole、Omeprazole、Hydrocortisone、Dexamethasone、Clarithromycin、Aprepitant、Loperamide、Saxagliptin、Empagliflozin 等

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 該適應症是遺傳易感性分類，不是可治療的疾病狀態，高分很可能來自與原適應症（攝護腺癌）的重疊。

**若要推進需要：**
- 釐清「攝護腺癌／腦癌易感性」在臨床上要治療的具體族群與目標，例如帶有特定基因變異的攝護腺癌患者。
- 針對該族群進行文獻與試驗檢索，確認是否有 enzalutamide 的直接研究。
- 補齊作用機轉與香港仿單的警語、禁忌症資料，再進行安全性評估。
- 若要評估真正的新適應症，建議改以有機轉依據的候選疾病重新篩選，例如 AR 依賴性的良性攝護腺間質腫瘤，並先做前臨床驗證。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Xtandi (enzalutamide) prescribing information, Astellas Pharma US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b129fdc9-1d8e-425c-a5a9-8a2ed36dfbdf) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


---
layout: default
title: Zolazepam
parent: 僅模型預測 (L5)
nav_order: 957
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Zolazepam：預測新適應症為失眠症 (Insomnia)（證據等級 L5）。原適應症：許可證未載明適應症（獸醫用注射劑，用於動物麻醉與鎮靜）"
monitor_inn: "Zolazepam"
predicted_indications: ["insomnia (disease)"]
---

# Zolazepam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Zolazepam：從獸醫麻醉鎮靜到失眠症
{: .text-alpha }

## 一句話總結

Zolazepam 是一種類苯二氮平（pyrazolodiazepinone）化合物，在香港僅以獸醫用藥上市，與 tiletamine 組成複方（Zoletil）用於動物麻醉與鎮靜。
TxGNN 模型預測它可能對**失眠症 (Insomnia)** 有效，但目前**沒有臨床試驗與文獻**支持，僅有模型預測與類別藥理推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明適應症（獸醫用注射劑，用於動物麻醉與鎮靜） |
| 預測新適應症 | 失眠症 (Insomnia) |
| TxGNN 預測分數 | 0.9988 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Zolazepam 詳細的作用機轉資料。根據已知資訊，Zolazepam 屬於類苯二氮平類化合物，在獸醫領域與 tiletamine 組成固定複方，用於麻醉與鎮靜。

苯二氮平類藥物會增強 GABA-A 受體訊號傳遞，產生鎮靜與助眠作用，這也是此類藥物用於失眠治療的既有機轉。因此，以類別類推的角度，TxGNN 給出高分預測在生物學上有其合理性。

但需要注意：這個關聯是由類別藥理**推論**而來，並非針對 Zolazepam 本身所證實。目前沒有任何 Zolazepam 專屬的機轉研究或人體臨床資料，且它僅以獸醫複方形式存在，並無人用製劑。

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
| HK-47383 | ZOLETIL 100 FOR INJECTION (VET) | 複方 | VIRBAC H.K. TRADING LIMITED | 有效 |
| HK-43831 | ZOLETIL 50 FOR INJ (VET) | 複方 | VIRBAC H.K. TRADING LIMITED | 有效 |

<!-- licenses:end -->

上表許可證皆為複方（tiletamine 與 zolazepam），持證商為 VIRBAC H.K. TRADING LIMITED，且均為獸醫用產品；狀態見表中「狀態」欄。

<!-- review:begin hk-lic-20261124b-zolazepam-1 -->

> **查核更正（2026-11-24）**：原文為「兩張許可證皆為單一成分登記、狀態有效，持證商為 VIRBAC H.K. TRADING LIMITED，且均為獸醫用產品。」。已更正：依衞生署藥物辦公室註冊名單的成分欄，含本藥成分的許可證皆為複方；原句的單一成分／複方說法或張數跟註冊名單不符（舊報告依證據包以「;;」切成分，每張都算成單方）。張數見本頁快速總覽與許可證表（2026-11-24 核對）。依據：[衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261124b-zolazepam-1 -->

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 證據僅停留在模型預測與類別藥理推論（L5），沒有任何臨床試驗或文獻支持。
- 目前僅有獸醫用製劑上市，缺乏人用安全性、劑型與給藥途徑的資料；且已有許多成熟的苯二氮平類藥物可用於失眠，需要有明確理由才值得投入。

**若要推進需要：**
- 取得 Zolazepam 的作用機轉資料（如受體結合與藥理特性）
- 取得原廠仿單的警語、禁忌與藥物交互作用資訊
- 進行文獻與臨床試驗登記的系統性檢索，確認是否有人體使用資料
- 評估單一成分的人用製劑可行性與給藥途徑
- 與現有苯二氮平類失眠藥物比較，釐清其潛在優勢

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-24 | 「兩張許可證皆為單一成分登記、狀態有效，持證商為 VIRBAC H.K. TRAD」→「上表許可證皆為複方（tiletamine 與 zolazep」 | 更正 | [衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


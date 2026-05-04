---
layout: default
title: Abacavir
parent: 僅模型預測 (L5)
nav_order: 11
evidence_level: L5
indication_count: 3
---

# Abacavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# ABACAVIR：從 HIV 感染到貓後天免疫缺乏症候群

## 一句話總結

Abacavir 是一種核苷酸逆轉錄酶抑制劑（NRTI），在全球廣泛用於人類免疫缺乏病毒（HIV）感染的治療，但目前在台灣尚未取得上市許可。TxGNN 模型預測它可能對**貓後天免疫缺乏症候群（Feline Acquired Immunodeficiency Syndrome，FIV 感染）**有效，目前有 **1 篇文獻**支持此方向，且無相關臨床試驗登記。值得注意的是，此預測適應症屬於獸醫領域，而非人類疾病。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV 感染（人類免疫缺乏病毒感染）|
| 預測新適應症 | 貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome) |
| TxGNN 預測分數 | 99.79% |
| 證據等級 | L4（僅有前臨床/體外研究） |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Abacavir 是一種核苷類逆轉錄酶抑制劑（Nucleoside Reverse Transcriptase Inhibitor, NRTI），透過競爭性抑制逆轉錄酶活性，阻斷逆轉錄病毒（Retrovirus）將 RNA 轉錄為 DNA 的過程，從而抑制病毒複製。

貓免疫缺乏病毒（FIV）與人類 HIV 同屬逆轉錄病毒科，在分子層面具有高度相似性，因此抑制 HIV 逆轉錄酶的藥物在理論上亦可能對 FIV 產生抑制效果。這也是為何 FIV/貓模型長期以來被作為 HIV 感染的動物模型進行研究。

然而，此預測適應症（貓後天免疫缺乏症候群）屬於**獸醫適應症**，並非人類疾病範疇。現有文獻證據亦以體外（in vitro）研究為主，尚未進入臨床試驗階段。若目標為人類疾病的藥物再利用，此預測的直接轉譯價值有限。

---

## 文獻證據

### 預測適應症 1：貓後天免疫缺乏症候群

| PMID | 年份 | 期刊 | 主要發現 |
|------|------|------|---------|
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Antiviral Research | 體外研究：ZDV + 3TC + Abacavir 三合一療法可抑制 FIV 複製，驗證了 NRTI 類藥物對 FIV 的活性 |

### 預測適應症 2：猿猴免疫缺乏病毒感染（SIV）

| PMID | 年份 | 期刊 | 主要發現 |
|------|------|------|---------|
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | Antiviral Therapy | 評估 16 種抗 HIV 藥物（含 Abacavir）對 HIV-2、SIV 及 SHIV 株的體外抗病毒活性，提供治療與暴露後預防用藥的參考依據 |

---

## 台灣上市資訊

Abacavir 在台灣目前**無上市許可登記**，未取得任何藥品許可證。若需進一步評估，需先取得台灣食藥署（TFDA）的相關仿單資料，或參考 EMA/FDA 核准仿單作為安全性參考依據。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ 注意：Abacavir 全球已知的重要警示包括 **HLA-B\*5701 相關超敏反應（hypersensitivity reaction）**，建議用藥前進行基因檢測，但此資訊未包含於本 Evidence Pack，需另行查閱 FDA/EMA 核准仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 模型所預測的兩個高分適應症（貓後天免疫缺乏症候群、猿猴免疫缺乏病毒感染）均屬於**動物疾病（獸醫適應症）**，而非人類疾病的藥物再利用方向，缺乏直接的臨床轉譯意義。現有文獻僅有 2 篇體外研究，無人體臨床試驗支撐，且 Abacavir 在台灣未取得上市許可，安全性資料存在明顯缺口。

**若要推進需要：**
- **確認再利用方向**：釐清目標是獸醫用途（FIV 治療）還是人類疾病（如 HIV-2 或其他逆轉錄病毒感染），兩者評估路徑截然不同
- **補足安全性資料**：下載並解析 FDA/EMA 核准 Abacavir 仿單，尤其是 HLA-B\*5701 超敏反應風險的相關資訊
- **補充 MOA 資料**：查詢 DrugBank API 取得完整作用機轉資訊，以強化機轉關聯性分析
- **擴大文獻搜索**：針對 NRTI 類藥物在 FIV 動物模型中的研究進行系統性回顧，評估是否有更完整的動物試驗資料
- **評估台灣上市可行性**：若目標為人類適應症，需先評估 Abacavir 在台灣申請上市的可行性與所需資源

---

> ⚠️ **免責聲明**：本報告結果僅供研究參考，不構成醫療建議。所有老藥新用候選需經過臨床驗證才能實際應用於患者。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


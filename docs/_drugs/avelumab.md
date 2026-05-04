---
layout: default
title: Avelumab
parent: 僅模型預測 (L5)
nav_order: 74
evidence_level: L5
indication_count: 10
---

# Avelumab
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

# Avelumab：從 Merkel 細胞癌 到 HHV-8 相關腫瘤

## 一句話總結

Avelumab 是一種抗 PD-L1 免疫檢查點抑制劑，已在多個國家取得 Merkel 細胞癌及局部晚期／轉移性尿路上皮癌維持治療的核准，但目前在香港尚未上市。TxGNN 模型將 **HHV-8 相關腫瘤 (human herpesvirus 8-related tumor)** 列為第一優先預測新適應症（預測分數 99.97%），然而此適應症目前**完全缺乏**直接臨床試驗與文獻佐證，預測純屬計算推演，尚無法推進至評估階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港未上市（FDA 核准：Merkel 細胞癌、尿路上皮癌一線維持治療） |
| 預測新適應症 | HHV-8 相關腫瘤 (human herpesvirus 8-related tumor) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Avelumab 為全人源 IgG1λ 單株抗體，透過選擇性結合 PD-L1，阻斷 PD-L1 與 PD-1 及 CD80 的交互作用，進而解除腫瘤微環境中的 T 細胞免疫抑制；此外其 Fc 段保留抗體依賴性細胞毒性（ADCC）效應，此點有別於部分其他 PD-L1 抑制劑。目前缺乏完整的作用機轉文件（MOA 資料尚待補充），以上描述係根據已知藥理類別整理。

HHV-8 相關腫瘤涵蓋卡波西肉瘤（Kaposi's Sarcoma）、原發性滲出性淋巴瘤（Primary Effusion Lymphoma, PEL）及多中心 Castleman 病（Multicentric Castleman Disease, MCD）。這些疾病的共同特徵是 HHV-8 病毒誘導的免疫逃逸——HHV-8 編碼的病毒性 IL-6（vIL-6）等免疫調節蛋白可能導致腫瘤細胞表面 PD-L1 上調，理論上為 PD-L1 阻斷提供治療窗口。

然而，此機轉連結目前屬高度推測性。TxGNN 的高分主要反映知識圖譜中免疫調節相關節點的廣泛拓撲連結，並非疾病特異性的實驗數據佐證。目前完全缺乏任何確認 Avelumab（或其他 PD-L1 抑制劑）在 HHV-8 相關腫瘤中之療效、PD-L1 表現率或免疫微環境特性的臨床前或臨床研究，機轉假設尚待實驗驗證，風險屬偽陽性預測。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Avelumab 目前在香港未取得任何藥品許可證，無上市記錄可供參考。若日後需在香港使用，須另行評估特殊用藥申請（名冊藥物／恩恤用藥）的可行性。

---

## 細胞毒性

Avelumab 為抗腫瘤生物製劑（免疫治療），適用本章節。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 免疫治療（Immune Checkpoint Inhibitor，抗 PD-L1 全人源單株抗體） |
| 骨髓抑制風險 | 低（非傳統細胞毒性機轉，骨髓抑制非主要毒性類型） |
| 致吐性分級 | 低 |
| 監測項目 | 肝腎功能、甲狀腺功能（TSH、fT4）、空腹血糖、腎上腺功能、CBC（含分類）、免疫相關不良反應（irAE）症狀監測 |
| 處置防護 | 靜脈輸注生物製劑標準流程；免疫相關不良反應（irAE）需早期識別、及時類固醇介入，嚴重者需永久停藥；請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
此預測完全來自計算模型推演（L5 等級），缺乏任何臨床試驗、體外實驗或文獻直接支持 Avelumab 在 HHV-8 相關腫瘤中的療效。同時，Avelumab 在香港尚未上市，進入臨床評估前需同時克服監管障礙，目前不具備推進條件。

**若要推進需要：**
- **生物標誌物研究**：確認 HHV-8 相關腫瘤（尤其是卡波西肉瘤）的 PD-L1 表現率及腫瘤免疫微環境特性
- **文獻搜尋**：系統回顧其他 PD-1/PD-L1 抑制劑（如 Pembrolizumab、Nivolumab）在卡波西肉瘤的已發表病例報告或 Phase 1/2 研究，以作間接外推依據
- **前臨床研究**：驗證 PD-L1 阻斷在 HHV-8 相關腫瘤細胞模型中的抑制效應
- **完整安全性資料**：取得 Avelumab 仿單全文，以完成 S1 安全性初評（目前為 Blocking 資料缺口）
- **監管評估**：評估 Avelumab 在香港申請特殊許可或恩恤用藥的可行性

> **附註：本次 Evidence Pack 包含 10 項預測適應症（multi 模式）。其中 Rank 9（前列腺尿道尿路上皮癌，L3，Proceed with Guardrails）具備 Phase 3 RCT 間接外推依據，Rank 10（腎盂肉瘤樣移行細胞癌，L4，Research Question）有 1 項觀察性研究登記，如需進一步評估，建議優先針對這兩項較具證據基礎的適應症另行撰寫專項報告。**

---

> ⚠️ **研究免責聲明**：本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用於臨床實踐。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

